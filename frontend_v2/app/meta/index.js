export default function Meta({ canonical, metaDescription, title }) {
  return (
    <>
      <title key="title">{title}</title>
      {/* <meta name="description" content={metaDescription} key="description" />
        <meta
          name="twitter:description"
          content={metaDescription}
          key="twitter:description"
        />
        <meta name="twitter:title" content={title} key="twitter:title" />
        <meta name="twitter:url" content={canonical} key="twitter:url" />
        <meta
          property="og:description"
          content={metaDescription}
          key="og:description"
        />
        <meta property="og:title" content={title} key="og:title" />
        <meta property="og:url" content={canonical} key="og:url" /> */}
    </>
  );
}
