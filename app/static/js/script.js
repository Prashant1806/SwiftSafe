// Get the form elements
const compareForm = document.querySelector('#compare-form');
const reportForm = document.querySelector('#report-form');

// Handle form submission
compareForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const formData = new FormData(compareForm);
  const formDataObj = Object.fromEntries(formData.entries());
  // Make a request to the server with the form data
  fetch('/compare', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formDataObj),
  })
  .then(response => response.json())
  .then(data => {
    // Update the results section with the match percentage
    const resultSection = document.querySelector('#results');
    resultSection.innerHTML = `<h2>Match Percentage: ${data.match_percentage}%</h2>`;
  })
  .catch(error => console.error(error));
});

reportForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const formData = new FormData(reportForm);
  const formDataObj = Object.fromEntries(formData.entries());
  // Make a request to the server with the form data
  fetch('/report', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formDataObj),
  })
  .then(response => response.json())
  .then(data => {
    // Show a success message
    alert('Report submitted successfully!');
    // Clear the form inputs
    reportForm.reset();
  })
  .catch(error => console.error(error));
});
