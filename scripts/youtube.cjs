const fs = require('fs/promises');
const path = require('path');
const { google } = require('googleapis');
require('dotenv').config();

const API_KEY = process.env.API_KEY;
const CHANNEL_ID = process.env.CHANNEL_ID;
const youtube = google.youtube('v3');

const outputPath = path.join(__dirname, '..', 'src', 'config', 'youtube.json');

const searchParams = {
  key: API_KEY,
  channelId: CHANNEL_ID,
  order: 'date',
  part: 'snippet',
  maxResults: 15,
  type: 'video',
};

function parseDuration(duration) {
  if (!duration) {
    return Number.POSITIVE_INFINITY;
  }

  const match = duration.match(/PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/);

  if (!match) {
    return Number.POSITIVE_INFINITY;
  }

  const hours = parseInt(match[1] || 0, 10);
  const minutes = parseInt(match[2] || 0, 10);
  const seconds = parseInt(match[3] || 0, 10);

  return hours * 3600 + minutes * 60 + seconds;
}

async function fetchLatestVideos() {
  const { data: searchData } = await youtube.search.list(searchParams);
  const items = searchData.items ?? [];

  const videoIds = items.map((item) => item.id?.videoId).filter(Boolean);

  if (videoIds.length === 0) {
    return [];
  }

  const { data: videoData } = await youtube.videos.list({
    key: API_KEY,
    part: 'snippet,contentDetails',
    id: videoIds.join(','),
  });

  const videos = videoData.items ?? [];

  return videos
    .filter((video) => {
      const liveStatus = video.snippet?.liveBroadcastContent;
      if (liveStatus && liveStatus !== 'none') {
        return false;
      }

      const durationSeconds = parseDuration(video.contentDetails?.duration);
      return Number.isFinite(durationSeconds) && durationSeconds >= 120 && durationSeconds <= 1200;
    })
    .sort((a, b) => new Date(b.snippet?.publishedAt || 0) - new Date(a.snippet?.publishedAt || 0))
    .slice(0, 5)
    .map((video) => ({
      title: video.snippet?.title,
      description: video.snippet?.description,
      channelId: video.snippet?.channelId,
      channelTitle: video.snippet?.channelTitle,
      videoId: video.id,
      thumbnails: video.snippet?.thumbnails,
      publishedAt: video.snippet?.publishedAt,
      duration: video.contentDetails?.duration,
    }));
}

async function main() {
  if (!API_KEY || !CHANNEL_ID) {
    console.warn('API_KEY o CHANNEL_ID no definidos, se usará youtube.json existente.');
    return;
  }

  try {
    const videos = await fetchLatestVideos();
    await fs.writeFile(outputPath, JSON.stringify(videos, null, 2));
    console.log('Los datos se han guardado en youtube.json');
  } catch (error) {
    console.error('Error al obtener datos de YouTube:', error.message);
    try {
      await fs.access(outputPath);
      console.warn('Usando youtube.json existente como fallback.');
    } catch {
      await fs.writeFile(outputPath, JSON.stringify([], null, 2));
      console.warn('Se creó youtube.json vacío como fallback.');
    }
  }
}

main();
