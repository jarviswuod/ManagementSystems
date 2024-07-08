import { useLoaderData } from "react-router-dom";
const LeaguesPage = () => {
  const leauges = useLoaderData();
  let leaugePosition = 1;

  return (
    <section>
      <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                #
              </th>
              <th scope="col" className="px-6 py-3">
                name
              </th>
              <th scope="col" className="px-6 py-3">
                founded
              </th>
              <th scope="col" className="px-6 py-3">
                country
              </th>
              <th scope="col" className="px-6 py-3">
                number of teams
              </th>
            </tr>
          </thead>
          <tbody>
            {leauges.map((leauge) => (
              <tr
                key={leauge.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                <th className="px-6 py-4">{leaugePosition++}</th>
                <th
                  scope="row"
                  className="px-6 py-4 font-medium flex gap-3 items-center text-gray-900 whitespace-nowrap dark:text-white"
                >
                  {leauge.name}
                </th>

                {/* <td className="px-6 py-4">{leauge.name}</td> */}
                <td className="px-6 py-4">{leauge.founded}</td>
                <td className="px-6 py-4">{leauge.country}</td>
                <td className="px-6 py-4">{leauge.number_of_teams}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};

const leaguesLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/league");
  const data = await res.json();
  return data;
};

export { LeaguesPage as default, leaguesLoader };
