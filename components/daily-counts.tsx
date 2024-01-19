import { DAILY_COUNTS_DATA } from "@/util/constants";
import { Card, LineChart, Title } from "@tremor/react";

const valueFormatter = (number: number) => `${number} listens`;

const DailyCounts = () => (
  <Card>
    <Title>Daily Song Counts over Time</Title>
    <LineChart
      className="mt-6"
      data={DAILY_COUNTS_DATA}
      index="date"
      categories={["Number of Songs"]}
      colors={["emerald"]}
      valueFormatter={valueFormatter}
      yAxisWidth={60}
    />
  </Card>
);

export default DailyCounts;
