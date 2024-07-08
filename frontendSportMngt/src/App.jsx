import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";

import HomePage, { standingTableLoader } from "./pages/HomePage";
import MainLayout from "./layouts/MainLayout";
import NotFoundPage from "./pages/NotFoundPage";
import NewsPage, { newsLoader } from "./pages/NewsPage";
import PlayerPage, { playerLoader } from "./pages/PlayerPage";
import GamesPage, { gamesLoader } from "./pages/GamesPage";
import LeaguesPage, { leaguesLoader } from "./pages/LeaguesPage";
import TeamsPage, { teamsLoader } from "./pages/TeamsPage";

import PlayersManagersPage, {
  PlayersManagersLoader,
} from "./pages/PlayersManagersPage";

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<MainLayout />}>
        <Route index element={<HomePage />} loader={standingTableLoader} />
        <Route path="/news" element={<NewsPage />} loader={newsLoader} />
        <Route path="/games" element={<GamesPage />} loader={gamesLoader} />
        <Route
          path="/leagues"
          element={<LeaguesPage />}
          loader={leaguesLoader}
        />
        <Route path="/teams" element={<TeamsPage />} loader={teamsLoader} />
        <Route
          path="/players"
          element={<PlayersManagersPage />}
          loader={PlayersManagersLoader}
        />
        <Route
          path="/players/:id"
          element={<PlayerPage />}
          loader={playerLoader}
        />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    )
  );
  return <RouterProvider router={router} />;
};

export default App;
