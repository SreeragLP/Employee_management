
document.addEventListener("DOMContentLoaded", function () {
    console.log("Dynamic Forms script loaded!");

    const formFieldsContainer = document.getElementById("formFields");
    const addFieldBtn = document.getElementById("addFieldBtn");
    const saveFormBtn = document.getElementById("saveFormBtn");

    // Initialize SortableJS for smooth drag-and-drop
    const sortable = new Sortable(formFieldsContainer, {
        animation: 150,  // Smooth dragging
        handle: ".drag-handle",
        ghostClass: "dragging",  // Class for dragged element
    });

    addFieldBtn.addEventListener("click", function () {
        const fieldWrapper = document.createElement("div");
        fieldWrapper.classList.add("mb-3", "field-group", "d-flex", "align-items-center", "draggable");

        // Drag Handle
        const dragHandle = document.createElement("span");
        dragHandle.classList.add("drag-handle", "me-2");
        dragHandle.innerHTML = "☰"; // Simple drag icon

        const labelInput = document.createElement("input");
        labelInput.type = "text";
        labelInput.placeholder = "Field Label";
        labelInput.classList.add("form-control", "me-2");

        const inputTypeSelect = document.createElement("select");
        inputTypeSelect.classList.add("form-select", "me-2");

        const inputTypes = ["text", "number", "date", "password", "email", "checkbox", "radio"];
        inputTypes.forEach(type => {
            const option = document.createElement("option");
            option.value = type;
            option.textContent = type.charAt(0).toUpperCase() + type.slice(1);
            inputTypeSelect.appendChild(option);
        });

        const removeBtn = document.createElement("button");
        removeBtn.textContent = "X";
        removeBtn.classList.add("btn", "btn-danger", "remove-btn");
        removeBtn.addEventListener("click", function () {
            fieldWrapper.remove();
        });

        fieldWrapper.appendChild(dragHandle);
        fieldWrapper.appendChild(labelInput);
        fieldWrapper.appendChild(inputTypeSelect);
        fieldWrapper.appendChild(removeBtn);
        formFieldsContainer.appendChild(fieldWrapper);
    });

    saveFormBtn.addEventListener("click", function () {
        const formName = prompt("Enter form name (e.g., 1, 2, 3):");
        if (!formName) return alert("Form name is required!");

        const fields = [];
        document.querySelectorAll(".field-group").forEach(field => {
            const label = field.querySelector("input").value.trim();
            const inputType = field.querySelector("select").value;

            if (label) {
                fields.push({ label, inputType });
            }
        });

        if (fields.length === 0) return alert("At least one field is required!");

        fetch("/dashboard/save_dynamic_form/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ form_name: formName, fields: fields })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert("Form saved successfully!");
                window.location.reload();
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
