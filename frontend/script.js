const apiUrl = 'http://your-ec2-public-ip:5000/employees';

// Fetch and display one employee
async function fetchEmployee() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    const employee = data.employees[Math.floor(Math.random() * data.employees.length)];
    document.getElementById('employee-container').innerHTML = `
      <p><strong>Name:</strong> ${employee.name}</p>
      <p><strong>Position:</strong> ${employee.position}</p>
      <p><strong>Department:</strong> ${employee.department}</p>
    `;
  } catch (error) {
    console.error("Error fetching employee:", error);
  }
}

// Fetch and display all employees
async function fetchAllEmployees() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    let html = "<h2>All Employees</h2>";
    data.employees.forEach(employee => {
      html += `
        <p><strong>Name:</strong> ${employee.name} - <strong>Position:</strong> ${employee.position} - <strong>Department:</strong> ${employee.department}</p>
      `;
    });
    document.getElementById('employee-container').innerHTML = html;
  } catch (error) {
    console.error("Error fetching all employees:", error);
  }
}
