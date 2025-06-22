import React from "react";

import styles from "./Hero.module.css";
import data from "../../data/info.json"
import { getImageUrl } from "../../utils";



export const Hero = () => {
  return (
    <section className={styles.container}>
      <div className={styles.content}>
        <h1 className={styles.title}>{`Hey, I'm ${data.name.split(" ")[0]}`}</h1>
        <p className={styles.description}>
          {data.bio}
        </p>
      </div>
      <div className={styles.topBlur} />
      <div className={styles.bottomBlur} />
    </section>
  );
};
