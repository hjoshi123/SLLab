/**
 * @author Hemant Joshi
 */

//check to call mouseover() only once
let check = 0;
window.onload = () => {
  const hospitalDetails = [
    {
      name: 'Columbia Asia',
      location: 'Bengaluru',
    }
  ];

  hospitalDetails.forEach((item, index) => {
    document.getElementById('hosp_title').innerHTML =  `Hospital Name: ${hospitalDetails[index].name}`;
    document.getElementById('hosp_loc_tit').innerHTML = `Hospital Location: ${hospitalDetails[index].location}`;
  });
};

function mouseover() {
  check += 1;
  if (check == 1) {
    const table = document.getElementById('patient');
    table.removeAttribute('hidden');
  
    const patientDetails = [
      {
        name: 'Pablo Escobar',
        aadhar: '300900010023',
        tests: ['prostate', 'blood'],
      },
      {
        name: 'El Chapo',
        aadhar: '0100100001000',
        tests: ['blood', 'body'],
      }
    ];
    const header = table.createTHead();
    const row = header.insertRow(0);
    row.insertCell(0).innerHTML = `<b>Patient's Name</b>`;
    row.insertCell(1).innerHTML = `<b>Patient's Aadhar</b>`;
    row.insertCell(2).innerHTML = `<b>Patient's Tests</b>`;
  
    for (let i = 0; i < patientDetails.length; i++) {
      let tests = '';
      const row = table.insertRow(i + 1);
      row.insertCell(0).innerHTML = patientDetails[i].name;
      row.insertCell(1).innerHTML = patientDetails[i].aadhar;
      for (j in patientDetails[i].tests) {
        tests += ` ${patientDetails[i].tests[j]}, `;
      }
      row.insertCell(2).innerHTML = tests;
    }
  }
}
