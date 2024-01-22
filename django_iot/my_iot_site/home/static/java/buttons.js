/* Function for turning lights off and on */
// eslint-disable-next-line no-unused-vars
function getOnOff (zone, payload) {
  fetch(`http://localhost:8080/zigbee/?topic=zigbee2mqtt/${zone}/set&payload=${payload}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      return response.json()
    })
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error))
}
