import React from "react";

import styles from "./ProjectCard.module.css";

export const ProjectCard = ({
  project: { project_name, description, technologies, link, githubLink },
}) => {
  return (
    <div className={styles.container}>
      <h3 className={styles.title}>{project_name}</h3>
      <p className={styles.description}>{description}</p>
      <ul className={styles.skills}>
        {technologies.map((skill, id) => {
          return (
            <li key={id} className={styles.skill}>
              {skill}
            </li>
          );
        })}
      </ul>
      <div className={styles.links}>
        {link != null &&
          <a href={link} className={styles.link}>Demo</a>
        }
        {githubLink != null &&
          <a href={githubLink} className={styles.link}>
            Source
          </a>
        }
      </div>
    </div>
  );
};
