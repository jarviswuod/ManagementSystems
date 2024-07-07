import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";

import HomePage from "./pages/HomePage";
import MainLayout from "./layouts/MainLayout";
import NotFoundPage from "./pages/NotFoundPage";
import NewsPage, { newsLoader } from "./pages/NewsPage";
import PlayersManagersPage, {
  PlayersManagersLoader,
} from "./pages/PlayersManagersPage";
import PlayerPage, { playerLoader } from "./pages/PlayerPage";

const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path="/news" element={<NewsPage />} loader={newsLoader} />
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
