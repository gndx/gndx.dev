export const createOgImage = ({
  title,
  meta,
}: {
  title: string;
  meta: string;
}) =>
  [
    // ACCOUNT PREFIX
    // Add your own Cloudinary account ID.
    `https://res.cloudinary.com/gndxdev/image/upload`,
    // Composed Image Transformations
    `w_960,h_502,q_70`,
    // TITLE
    // Karla google font in light rose
    `l_text:Ubuntu_56_bold:${e(title)},co_rgb:ffe4e6,c_fit,w_750,h_100`,
    // Positioning
    `fl_layer_apply,g_south_west,x_100,y_240`,
    // META
    // Karla, but smaller
    `l_text:Ubuntu_32_bold:${e(meta)},co_rgb:ffe4e680,c_fit,w_500`,
    // Positioning
    `fl_layer_apply,g_south_west,x_100,y_100`,
    // BG
    `gndx-dev-og-2024.png`,
  ].join("/");

// double escape for commas and slashes
const e = (str: string) => encodeURIComponent(encodeURIComponent(str));
