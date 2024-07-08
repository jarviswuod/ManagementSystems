import { useLoaderData } from "react-router-dom";
import { formatDistanceToNow } from "date-fns";

const NewsPage = () => {
  const news = useLoaderData();

  function timeAgo(timestamp) {
    const date = new Date(timestamp);
    return formatDistanceToNow(date, { addSuffix: true });
  }

  return (
    <section className="flex items-center justify-center">
      <div>
        {news.map((singlenews) => (
          <div
            key={singlenews.id}
            className="max-w-xl p-6 bg-white  rounded-lg dark:bg-gray-800 dark:border-gray-700"
          >
            <h5 className="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">
              {singlenews.headline}
            </h5>

            <p className="mb-3 font-normal text-gray-500 dark:text-gray-400">
              {singlenews.content}
            </p>
            <p className="inline-flex font-medium items-center text-gray-500 dark:text-gray-400 mb-3">
              {singlenews.writer_id.first_name} ({timeAgo(singlenews.timestamp)}
              )
            </p>
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
