import { useLoaderData } from "react-router-dom";
import { formatDistanceToNow } from "date-fns";

const NewsPage = () => {
  const news = useLoaderData();

  function timeAgo(timestamp) {
    const date = new Date(timestamp);

    return formatDistanceToNow(date, { addSuffix: true });
  }

  return (
    <section>
      <div>
        <h2>News</h2>
        {news.map((singlenews) => (
          <div key={singlenews.id}>
            <div>{singlenews.content}</div>
            <div>{timeAgo(singlenews.timestamp)}</div>
            <div>{singlenews.writer_id}</div>
          </div>
        ))}
      </div>
    </section>
  );
};

const newsLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/communication");
  const data = await res.json();
  return data;
};

export { NewsPage as default, newsLoader };
