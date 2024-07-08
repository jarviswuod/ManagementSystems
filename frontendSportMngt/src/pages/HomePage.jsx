import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { useLoaderData } from "react-router-dom";

const HomePage = () => {
  const tableData = useLoaderData();
  let teamPosition = 1;

  return (
    <section>
      <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                Position
              </th>
              <th scope="col" className="px-6 py-3">
                Club
              </th>

              <th scope="col" className="px-6 py-3">
                played
              </th>
              <th scope="col" className="px-6 py-3">
                won
              </th>
              <th scope="col" className="px-6 py-3">
                draw
              </th>

              <th scope="col" className="px-6 py-3">
                lost
              </th>

              <th scope="col" className="px-6 py-3">
                points
              </th>
            </tr>
          </thead>
          <tbody>
            {tableData.map((team) => (
              <tr
                key={team.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                <th className="px-6 py-4">{teamPosition++}</th>
                <td
                  scope="row"
                  className="px-6 py-4 font-medium flex gap-3 items-center text-gray-900 whitespace-nowrap dark:text-white"
                >
                  <Avatar>
                    <AvatarImage src="https://github.com/shadcn.png" />
                    <AvatarFallback>
                      {team.team_id.name.slice(0, 3)}
                    </AvatarFallback>
                  </Avatar>
                  {team.team_id.name}
                </td>
                <td className="px-6 py-4">{team.games_played}</td>
                <td className="px-6 py-4">{team.wins}</td>
                <td className="px-6 py-4">{team.draws}</td>
                <td className="px-6 py-4">{team.lost}</td>
                <td className="px-6 py-4">{team.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};

const standingTableLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/teamseason");
  const data = await res.json();
  return data;
};
export { HomePage as default, standingTableLoader };
