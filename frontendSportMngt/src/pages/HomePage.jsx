import Standing, { standingLoader } from "@/components/Standing";

const HomePage = () => {
  return (
    <div>
      <Standing loader={standingLoader} />
    </div>
  );
};

export default HomePage;
