const apiUrl = 'http://localhost:8000/api'; // Replace with your API base URL

const getAuthToken = () => {
  return localStorage.getItem('barli-access-token');
};

const getRefreshToken = () => {
  return localStorage.getItem('barli-refresh-token');
}

export const setAuthToken = (token) => {
  localStorage.setItem('barli-access-token', token);
};

export const setRefreshToken = (token) => {
  localStorage.setItem('barli-refresh-token', token);
};

export const getClaimsFromToken = (token) => {
  const payloadEncodedB64 = token.split('.')[1];
  const decodedToken = JSON.parse(atob(payloadEncodedB64));
  return decodedToken;
}

const isTokenExpired = (token) => {
  const decodedToken = getClaimsFromToken(token);
  return decodedToken.exp * 1000 < Date.now(); // Convert seconds to milliseconds
};

export function logout() {
  localStorage.removeItem('barli-access-token');
  localStorage.removeItem('barli-refresh-token');
}

export async function login(data) {
  return fetch(`${apiUrl}/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
  })
}

export async function registerNewCustomerOrBar(data) {
  return fetch(`${apiUrl}/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
}

export async function getNumbers() {
  return fetchWithInterceptor('/obtener_numeros')
}

const fetchWithInterceptor = async (url, options) => {
  let authToken = getAuthToken();
  let refreshToken = getRefreshToken();

  if (authToken && isTokenExpired(authToken)) {
    try {
      // Fetch a new token using your refresh endpoint
      const refreshResponse = await fetch(`${apiUrl}/token/refresh`, {
        method: 'POST',
        body: JSON.stringify({"refresh": refreshToken}),
        headers: {
          'Content-Type': 'application/json'
        },
      });

      if (refreshResponse.ok) {
        const newTokenResponse = await refreshResponse.json();
        setAuthToken(newTokenResponse.access);
        authToken = getAuthToken();
      } else {
        // TODO: Handle refresh failure, e.g., redirect to login
        throw new Error('Token refresh failed');
      }
    } catch (error) {
      console.error('Error refreshing token:', error);
      // TODO: Handle error, e.g., redirect to login
      throw error;
    }
  }

  if (authToken) {
    if (!options) {
      options = {};
    }

    if (!options.headers) {
      options.headers = {};
    }
    options.headers['Authorization'] = `Bearer ${authToken}`;
  }

  return fetch(`${apiUrl}${url}`, options);
};
