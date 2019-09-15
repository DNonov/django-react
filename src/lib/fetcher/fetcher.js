import axios from 'axios';

/**
 * Wrapper around axios
 *
 * @param {Object} data
 * @returns {Promise}
 */
function fetcher(data={}) {
  return new Promise((resolve, reject) => {
    return axios(data)
      .then(response => {
        resolve(response);
      })
      .catch(e => reject(e));
  });
}

export default fetcher;