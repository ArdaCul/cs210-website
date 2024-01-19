"use client";
import styles from "./hero-section.module.scss";
import { useState } from "react";
import { motion } from "framer-motion";
import useMousePosition from "@/util/useMousePosition";

export default function HeroSection() {
  const [isHovered, setIsHovered] = useState(false);
  const { x, y } = useMousePosition();
  const size = isHovered ? 400 : 40;

  return (
    <main className={styles.main}>
      <motion.div
        className={styles.mask}
        animate={{
          WebkitMaskPosition: `${x - size / 2}px ${y - size / 2}px`,
          WebkitMaskSize: `${size}px`,
        }}
        transition={{ type: "tween", ease: "backOut", duration: 0.5 }}
      >
        <p
          onMouseEnter={() => {
            setIsHovered(true);
          }}
          onMouseLeave={() => {
            setIsHovered(false);
          }}
        >
          Please give me a high grade I need it 🥺
        </p>
      </motion.div>

      <div className={styles.body}>
        <p>
          This is <span>Arda Culhaci</span>'s submission for CS210 project.
          Scroll down and enjoy 😊
        </p>
      </div>
    </main>
  );
}
