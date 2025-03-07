import React, { useState } from "react";
import { createProject } from "../api";
import { useNavigate } from "react-router-dom";

const CreateProject = () => {
    const [project, setProject] = useState({
        project_name: "",
        wo_number: "",
        activity_code: "",
        total_labor_amount: 0,
        total_expenses_amount: 0,
        total_travel_amount: 0,
        total_tier_fee: 0,
        total_budget_amount: 0,
        subtasks: [],
    });

    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        await createProject(project);
        navigate("/");
    };

    return (
        <div>
            <h1>Create a New Project</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Project Name"
                    value={project.project_name}
                    onChange={(e) => setProject({ ...project, project_name: e.target.value })}
                    required
                />
                <input
                    type="text"
                    placeholder="WO Number"
                    value={project.wo_number}
                    onChange={(e) => setProject({ ...project, wo_number: e.target.value })}
                    required
                />
                <button type="submit">Create Project</button>
            </form>
        </div>
    );
};

export default CreateProject;
