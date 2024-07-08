import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Link, useLoaderData } from "react-router-dom";

import DateComponent from "@/components/DateComponent";
import TimeComponent from "@/components/TimeComponent";

const GamesPage = () => {
  const games = useLoaderData();

  return (
    <section>
      <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-center rtl:text-center text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                Date
              </th>
            </tr>
          </thead>
          <tbody>
            {games.map((game) => (
              <div
                key={game.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                {/* <DateComponent dateString={`${game.date}`} /> */}
                <div className="grid grid-cols-[1fr_60px_1fr] p-4 gap-4 items-center justify-center">
                  <div className="flex items-center justify-center gap-4 justify-self-end">
                    {game.home_team_id.name}
                    <Avatar>
                      <AvatarImage src="https://github.com/shadcn.png" />
                      <AvatarFallback>
                        {game.home_team_id.name.slice(0, 3)}
                      </AvatarFallback>
                    </Avatar>
                  </div>
                  <div>
                    {game.home_team_score == null ? (
                      <TimeComponent dateString={game.start_time} />
                    ) : (
                      <div className="flex items-center justify-center gap-2 border rounded bg-black py-2 text-base font-bold text-white">
                        <p>{game.home_team_score}</p>:
                        <p>{game.away_team_score}</p>
                      </div>
                    )}
                  </div>

                  <div className="flex items-center justify-center gap-4 justify-self-start">
                    <Avatar>
                      <AvatarImage src="https://github.com/shadcn.png" />
                      <AvatarFallback>
                        {game.away_team_id.name.slice(0, 3)}
                      </AvatarFallback>
                    </Avatar>
                    {game.away_team_id.name}
                  </div>
                </div>
              </div>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
};

const gamesLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/game");
  const data = await res.json();
  return data;
};

export { GamesPage as default, gamesLoader };
