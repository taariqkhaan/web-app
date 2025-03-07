import React, { useEffect, useState } from "react";
import { getProjects } from "../api";
import { Link } from "react-router-dom";

const Home = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        async function fetchProjects() {
            const data = await getProjects();
            setProjects(data);
        }
        fetchProjects();
    }, []);

    return (
        <div>
            <h1>Project Dashboard</h1>
            <Link to="/create">➕ Create New Project</Link>
            <ul>
                {projects.map((project) => (
                    <li key={project.id}>
                        <Link to={`/projects/${project.id}`}>{project.project_name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Home;
