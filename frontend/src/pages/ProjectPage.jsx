import React, { useEffect, useState } from "react";
import { getProjectById } from "../api";
import { useParams } from "react-router-dom";

const ProjectPage = () => {
    const { id } = useParams();
    const [project, setProject] = useState(null);

    useEffect(() => {
        async function fetchProject() {
            const data = await getProjectById(id);
            setProject(data);
        }
        fetchProject();
    }, [id]);

    if (!project) return <h2>Loading...</h2>;

    return (
        <div>
            <h1>{project.project_name}</h1>
            <p>WO Number: {project.wo_number}</p>
            <p>Activity Code: {project.activity_code}</p>
            <h2>Subtasks</h2>
            <ul>
                {project.subtasks.map((subtask, index) => (
                    <li key={index}>
                        {subtask.subtask_name} - ${subtask.budget_amount}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProjectPage;
