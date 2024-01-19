"use client";

import { use, useRef, useState } from "react";
import { Button, Card, DonutChart, Legend, Title } from "@tremor/react";
import { TOP_10_ARTISTS_PER_SEASON } from "@/util/constants";
import { PlayIcon, PauseIcon } from "@heroicons/react/16/solid";

const EMOJIS = {
  Fall: "🍂",
  Spring: "🌸",
  Summer: "🌞",
  Winter: "❄️",
};

const AUDIOS = {
  Fall: "/music/tyler.mp3#t=00:02:01",
  Spring: "/music/superhero.mp3",
  Summer: "/music/chris.mp3#t=00:00:35",
  Winter: "/music/chopin.mp3",
};

const seasonsColors = {
  Spring: [
    "indigo-900",
    "indigo-800",
    "indigo-700",
    "indigo-600",
    "indigo-500",
    "violet-900",
    "violet-800",
    "violet-700",
    "violet-600",
    "violet-500",
  ],
  Summer: [
    "lime-900",
    "lime-800",
    "lime-700",
    "lime-600",
    "lime-500",
    "amber-900",
    "amber-800",
    "amber-700",
    "amber-600",
    "amber-500",
  ],
  Fall: [
    "green-900",
    "green-800",
    "green-700",
    "green-600",
    "green-500",
    "teal-900",
    "teal-800",
    "teal-700",
    "teal-600",
    "teal-500",
  ],
  Winter: [
    "blue-900",
    "blue-800",
    "blue-700",
    "blue-600",
    "blue-500",
    "sky-900",
    "sky-800",
    "sky-700",
    "sky-600",
    "sky-500",
  ],
};

export const DonutChartComponent = ({
  season,
}: {
  season: "Fall" | "Spring" | "Summer" | "Winter";
}) => {
  const [isPlaying, setIsPlaying] = useState(false);

  const audioRef = useRef<HTMLAudioElement>(null);

  const play = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
        setIsPlaying(false);
      } else {
        audioRef.current.play();
        setIsPlaying(true);
      }
    } else {
      // Throw error
    }
  };

  return (
    <>
      <Card className="mx-auto max-w-xs">
        <Title>Top Artists</Title>
        <DonutChart
          className="mt-6"
          data={TOP_10_ARTISTS_PER_SEASON[season]}
          category="value"
          index="name"
          variant="donut"
          label={`${EMOJIS[season]} ${season}`}
          valueFormatter={(v) => ""}
          colors={seasonsColors[season]}
        />
        <Legend
          className="mt-3"
          categories={TOP_10_ARTISTS_PER_SEASON[season].map((a) => a.name)}
          colors={seasonsColors[season]}
        />
        <audio ref={audioRef} src={AUDIOS[season]} />
        <div className="flex flex-col mt-5">
          <Button
            icon={isPlaying ? PauseIcon : PlayIcon}
            color={seasonsColors[season][0]}
            onClick={play}
          >
            {isPlaying ? "Pause the music!" : "Have a taste of my music!"}
          </Button>
        </div>
      </Card>
    </>
  );
};
