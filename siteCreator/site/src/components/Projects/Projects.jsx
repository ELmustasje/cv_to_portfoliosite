import React from "react";

import styles from "./Projects.module.css";

import projects from "../../data/projects.json";
import data from "../../data/info.json";
import { ProjectCard } from "./ProjectCard";

const projectData = data["coding_projects"]

export const Projects = () => {
  return (
    <section className={styles.container} id="projects">
      <h2 className={styles.title}>Projects</h2>
      <div className={styles.projects}>
        {projectData.map((project, id) => {
          return <ProjectCard key={id} project={project} />;
        })}
      </div>
    </section>
  );
};
