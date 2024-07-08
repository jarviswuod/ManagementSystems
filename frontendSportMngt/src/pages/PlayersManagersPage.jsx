import { Link, useLoaderData } from "react-router-dom";

const PlayersManagersPage = () => {
  const playersInfor = useLoaderData();
  let playerPosition = 1;

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
                first name
              </th>
              <th scope="col" className="px-6 py-3">
                last name
              </th>
              <th scope="col" className="px-6 py-3">
                email
              </th>
              <th scope="col" className="px-6 py-3">
                date of birth
              </th>
              <th scope="col" className="px-6 py-3">
                role
              </th>
            </tr>
          </thead>
          <tbody>
            {playersInfor.map((player) => (
              <tr
                key={player.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                <th className="px-6 py-4">
                  <Link to={`/players/${player.id}`}> {playerPosition++} </Link>
                </th>
                <td className="px-6 py-4">{player.first_name}</td>
                <td className="px-6 py-4">{player.last_name}</td>
                <td className="px-6 py-4">{player.email}</td>
                <td className="px-6 py-4">{player.date_of_birth}</td>
                <td className="px-6 py-4">{player.role}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};

const PlayersManagersLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/playermanager");
  const data = await res.json();
  return data;
};

export { PlayersManagersPage as default, PlayersManagersLoader };
