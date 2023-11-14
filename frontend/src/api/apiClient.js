export async function login(username, password) {
  return fetch('http://localhost:8000/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({'username': username, 'password': password}),
  })
}

export async function registerNewCustomerOrBar(data) {
  return fetch('https://barli.free.beeceptor.com', {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
}

/*
export async function getBarList() {
  const response = await fetch('http://localhost:8000/api/bars', {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });
}
*/