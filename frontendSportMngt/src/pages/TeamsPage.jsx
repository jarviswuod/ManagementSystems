import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { useLoaderData } from "react-router-dom";
const TeamsPage = () => {
  const teams = useLoaderData();
  let teamPosition = 1;

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
                number of players
              </th>
              <th scope="col" className="px-6 py-3">
                ground
              </th>

              <th scope="col" className="px-6 py-3">
                location
              </th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team) => (
              <tr
                key={team.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                <th className="px-6 py-4">{teamPosition++}</th>
                <th
                  scope="row"
                  className="px-6 py-4 font-medium flex gap-3 items-center text-gray-900 whitespace-nowrap dark:text-white"
                >
                  <Avatar>
                    <AvatarImage src="https://github.com/shadcn.png" />
                    <AvatarFallback>
                      {team?.name.slice(0, 3).toUpperCase()}
                    </AvatarFallback>
                  </Avatar>
                  {team.name}
                </th>

                <td className="px-6 py-4">{team.founded}</td>
                <td className="px-6 py-4">{team.number_of_players}</td>
                <td className="px-6 py-4">{team.ground}</td>
                <td className="px-6 py-4">{team.location}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};
const teamsLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/team");
  const data = await res.json();
  return data;
};

export { TeamsPage as default, teamsLoader };
