import { parseISO, format } from "date-fns";

const TimeComponent = ({ dateString }) => {
  const date = parseISO(dateString);
  const formattedTime = format(date, "HH:mm");

  const hours = formattedTime.split(":")[0];
  const minutes = formattedTime.split(":")[1];

  return (
    <div className="flex items-center justify-center gap-2 border rounded bg-black py-2 text-base font-bold text-white">
      <p>{hours}</p>:<p>{minutes}</p>
    </div>
  );
};

export default TimeComponent;
