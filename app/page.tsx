"use client";

import DailyCounts from "@/components/daily-counts";
import { DonutChartComponent } from "@/components/donut-chart";
import { GroupBarChart } from "@/components/group-bar-chart";
import HeroSection from "@/components/hero-section";
import { ExclamationCircleIcon } from "@heroicons/react/16/solid";
import { Callout } from "@tremor/react";

export default function Home() {
  return (
    <div className="flex flex-col gap-10">
      <HeroSection />
      <div className="px-10 py-10 flex flex-col gap-10">
        <DailyCounts />
        <Callout
          className="mt-4"
          title="Conclusion"
          icon={ExclamationCircleIcon}
          color="teal"
        >
          The above graph shows that my day to day listens varied between 0 and
          80 listens on average, reaching a maximum of almost 160 listens
          towards the end of 2023 on the 8th of December.
        </Callout>
        <GroupBarChart />
        <Callout
          className="mt-4"
          title="Conclusion"
          icon={ExclamationCircleIcon}
          color="teal"
        >
          The above graph shows that my most-listened-to genre each season is
          always &quot;Album Rock&quot;. However, second place is held by
          &quot;Alternative Rock&quot; in Winter and Summer, whereas it is held
          by &quot;Australian Rock&quot; in Fall and Spring. Hence, it can be
          concluded that the season does not affect my music taste throughout
          the year.
        </Callout>
        <div className="grid grid-cols-4 gap-10">
          <DonutChartComponent season="Fall" />
          <DonutChartComponent season="Winter" />
          <DonutChartComponent season="Spring" />
          <DonutChartComponent season="Summer" />
        </div>
      </div>
    </div>
  );
}
