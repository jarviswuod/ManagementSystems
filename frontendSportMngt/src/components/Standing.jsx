import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { useLoaderData } from "react-router-dom";

const Standing = () => {
  const tableData = useLoaderData();
  console.log(tableData);

  return (
    <section>
      <div>Epl standing</div>

      <Table>
        <TableCaption>A list of your recent invoices.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px]">Invoice</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Method</TableHead>
            <TableHead className="text-right">Amount</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell className="font-medium">INV001</TableCell>
            <TableCell>Paid</TableCell>
            <TableCell>Credit Card</TableCell>
            <TableCell className="text-right">$250.00</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </section>
  );
};

const standingLoader = async ({ params }) => {
  const res = await fetch("http://127.0.0.1:8000/api/teamseason");
  const data = await res.json();
  return data;
};
export { Standing as default, standingLoader };
