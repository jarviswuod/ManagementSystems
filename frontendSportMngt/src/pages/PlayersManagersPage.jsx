import { Link, useLoaderData } from "react-router-dom";

const PlayersManagersPage = () => {
  const playersInfor = useLoaderData();

  return (
    <div>
      <h1>Players and Managers</h1>
      {playersInfor.map((player) => (
        <Link to={`/players/${player.id}`} key={player.id}>
          <p>{player.first_name}</p>
          <p>{player.last_name}</p>
          <p>{player.email}</p>
          <p>{player.contact}</p>
          <p>{player.date_of_birth}</p>
          <p>{player.gender}</p>
          <p>{player.salary}</p>
          <p>{player.jersey_no}</p>
          <p>{player.position}</p>
          <p>{player.role}</p>
        </Link>
      ))}
    </div>
  );
};

const PlayersManagersLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/playermanager");
  const data = await res.json();
  return data;
};

export { PlayersManagersPage as default, PlayersManagersLoader };
