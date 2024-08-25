function addStaff(project_id, csrf_token) {
    const emp = document.getElementById('input-add-staff');
    const data = {emp_id: emp.value};

    fetch(`/project/${project_id}/edit/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}

async function removeStaff(project_id, emp_id, csrf_token) {
    fetch(`/project/${project_id}/edit/${emp_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}
