import rss from '@astrojs/rss';
import config from "@config/config.json";
import { getPostsByLocale } from '@utils/i18nContent';

export async function GET(context) {
	const posts = await getPostsByLocale('es');
	return rss({
		title: config.site.title,
		description: config.site.description,
		site: context.site,
		customData: '<language>es</language>',
		items: posts.map((post) => ({
			title: post.data.title,
			description: post.data.description,
			pubDate: post.data.pubDate,
			categories: [...post.data.categories, ...post.data.tags],
			link: `/blog/${post.slug || post.id.replace(/\.(md|mdx)$/i, '')}/`,
		})),
	});
}
