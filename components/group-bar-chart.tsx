"use client";

import { TOP_5_GENRES } from "@/util/constants";
import { BarChart, Card, Title } from "@tremor/react";
import { useState } from "react";

export const GroupBarChart = () => {
  const [value, setValue] = useState(null);

  return (
    <>
      <Card>
        <Title>TOP FIVE LISTENED GENRES PER SEASON</Title>
        <BarChart
          className="mt-6"
          data={TOP_5_GENRES}
          index="name"
          categories={[
            "album rock",
            "alternative metal",
            "alternative rock",
            "australian rock",
            "classic rock",
            "grunge",
            "hard rock",
            "modern alternative rock",
            "modern rock",
          ]}
          yAxisWidth={80}
          onValueChange={(v) => setValue(v)}
          valueFormatter={(v: number) =>
            `${(v / 60).toLocaleString("en-US")} min`
          }
        />
      </Card>
    </>
  );
};
