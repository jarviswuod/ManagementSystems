import { parseISO, format } from "date-fns";

const DateComponent = ({ dateString }) => {
  const formattedDate = format(parseISO(dateString), "EEEE dd MMMM yyyy");

  return (
    <div>
      <p>{formattedDate}</p>
    </div>
  );
};

export default DateComponent;
