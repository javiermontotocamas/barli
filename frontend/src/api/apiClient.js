const apiUrl = 'http://localhost:8000/api' // Replace with your API base URL


//ZONA LOGIN
export const getAuthToken = () => {
  return localStorage.getItem('barli-access-token')
}

export const getRefreshToken = () => {
  return localStorage.getItem('barli-refresh-token')
}

export const setAuthToken = (token) => {
  localStorage.setItem('barli-access-token', token)
}

export const setRefreshToken = (token) => {
  localStorage.setItem('barli-refresh-token', token)
}

export const getClaimsFromToken = (token) => {
  const payloadEncodedB64 = token.split('.')[1]
  const decodedToken = JSON.parse(atob(payloadEncodedB64))
  return decodedToken
}

export const isTokenExpired = (token) => {
  const decodedToken = getClaimsFromToken(token)
  return decodedToken.exp * 1000 < Date.now() // Convert seconds to milliseconds
}

export function logout() {
  localStorage.removeItem('barli-access-token')
  localStorage.removeItem('barli-refresh-token')
}

export async function login(data) {
  return fetch(`${apiUrl}/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
}

// Get Bars
export const getBars = async() => {
  return fetchWithInterceptor(`/bar`);
}

// CREAR NUEVO USUARIO
export async function registerNewCustomerOrBar(data) {
  return fetch(`${apiUrl}/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  })
}


//ZONA MESAS
export const getTablesOfBar = async(barId) => {
  return fetchWithInterceptor(`/bar/${barId}/tables`);
}


//ZONA ANUNCIOS
export const getAdsOfBar = async(barId) => {
  return fetchWithInterceptor(`/bar/${barId}/ads`);
}
export const deleteAdOfBar = async(barId, adId) => {
  return fetchWithInterceptor(`/bar/${barId}/ads/${adId}`, {
    method: 'DELETE'
  });
}
export const createAdOfBar = async(data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/ads`,{
    method: 'POST',
    body: JSON.stringify(data.recordData),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

//ZONA CUENTA USUARIO
export const getDataOfUser = async(userId) => {
  return fetchWithInterceptor(`/user/${userId}/data`);
}
export const modDataOfUser = async(data) => {
  return fetchWithInterceptor(`/user/${data.userId}/data`,{
    method: 'PUT',
    body: JSON.stringify({
      recordData: data.recordData,
      username: data.username
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}


//ZONA CUENTA DE BAR
export const getDataOfBar = async(barId) => {
  return fetchWithInterceptor(`/bar/${barId}/data`);
}
export const modDataOfBar = async(data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/data`,{
    method: 'PUT',
    body: JSON.stringify({
      recordData: data.recordData,
      username: data.username
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

//ZONA MESAS DE BAR
export const createTableOfBar = async(data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/tables`,{
    method: 'POST',
    body: JSON.stringify(data.recordData),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}
export const deleteTableOfBar = async(data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/tables/${data.tableId}`, {
    method: 'DELETE'
  });
}

export const updateTableStatus = (data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/tables/${data.tableId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ newStatus: data.newStatus }), // Puedes ajustar los datos según tus necesidades
  });
}


//ZONA PAGINA RESERVA
export const getAbleBars = async(data) => {
  const queryParams = new URLSearchParams(data).toString();
  return fetchWithInterceptor(`/bar?${queryParams}`);
}

//PASOS RESERVA DE MESA
//1.-OBTENEMOS EL ID DE LA MESA DISPONIBLE CON LOS REQUISITOS
export const getTableforBook = async(data) => {
  const queryParams = new URLSearchParams(data.datosMesa).toString();
  return fetchWithInterceptor(`/bar/${data.barId}/tables?${queryParams}`, {
  });
}
//2.-PATCH EN EL QUE PASAMOS LA MESA A 'ESPERA DE CONFIRMACION'
export const pendTableBar = async(data) => {
  return fetchWithInterceptor(`/bar/${data.barId}/tables/${data.tableId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
  });
}
//3.-POST PARA CREAR LA RESERVA
export const postBook = async(data) => {
  return fetchWithInterceptor(`/user/${data.userId}/booking/${data.tableId}`,{
    method: 'POST',
    body: JSON.stringify({user_id: data.userId, table_id: data.tableId}),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

//COMPROBAR RESERVAS DEL USUARIO LOGEADO
export const checkUserBook = async(data) => {
  return fetchWithInterceptor(`/user/${data}/booking`);
}








const fetchWithInterceptor = async (url, options) => {
  let authToken = getAuthToken()
  let refreshToken = getRefreshToken()

  if (authToken && isTokenExpired(authToken)) {
    try {
      // Fetch a new token using your refresh endpoint
      const refreshResponse = await fetch(`${apiUrl}/token/refresh`, {
        method: 'POST',
        body: JSON.stringify({ refresh: refreshToken }),
        headers: {
          'Content-Type': 'application/json'
        }
      })

      if (refreshResponse.ok) {
        const newTokenResponse = await refreshResponse.json()
        setAuthToken(newTokenResponse.access)
        authToken = getAuthToken()
      } else {
        // TODO: Handle refresh failure, e.g., redirect to login
        throw new Error('Token refresh failed')
      }
    } catch (error) {
      console.error('Error refreshing token:', error)
      // TODO: Handle error, e.g., redirect to login
      throw error
    }
  }

  if (authToken) {
    if (!options) {
      options = {}
    }

    if (!options.headers) {
      options.headers = {}
    }
    options.headers['Authorization'] = `Bearer ${authToken}`
  }

  return fetch(`${apiUrl}${url}`, options)
}
