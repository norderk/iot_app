/* Function for turning lights off and on */
// eslint-disable-next-line no-unused-vars
function getOnOff (zone, payload) {
  /*`http://fast_api:80/zigbee/?topic=zigbee2mqtt/${zone}/set&payload=${payload}` <-- Inside docker network*/
  /*`http://localhost:2222/zigbee/?topic=zigbee2mqtt/${zone}/set&payload=${payload}` <-- On localhost*/
  fetch(`http://localhost:8001/zigbee/?topic=zigbee2mqtt/${zone}/set&payload=${payload}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      return response.json()
    })
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error))
}
