# **Developer's Guide: Socrata Open Data APIs**

This document provides the technical details required to interact with Socrata-powered REST APIs, such as data.cdc.gov, opendata.maryland.gov, and many other government open data portals.

## **0\. Guiding Principles for AI Implementation**

**This section provides explicit instructions for an AI assistant generating code based on this guide.**

### **Directive \#1: Live API Integration**

The primary goal is to generate code that performs a **live, real-time HTTP request** to a Socrata API endpoint. The final generated code **must not** contain simulated, mocked, or hardcoded data.

* **DO:** Write code that dynamically calls an HTTP client (e.g., requests in Python, fetch in JavaScript) at runtime to retrieve data.  
* **DO NOT:** Create a static variable or constant (e.g., const socrataData \= \[...\]) to represent the API's response. The data must be retrieved from the live endpoint.

### **Directive \#2: Verify Data Structure Before Coding**

Socrata API URLs (e.g., .../resource/9qyj-bhez.json) are identifiers and **do not describe the data they contain**. Assuming the data structure based on surrounding conversation or the URL's context can lead to significant errors.

* **ACTION:** If a user provides a Socrata URL without also providing a clear description or a sample data row, **you must ask for more context before writing code**. Specifically, request the following information from the user:  
  1. The **Dataset Title** from its page on the data portal.  
  2. A **copy of the first data object** from the raw JSON URL.  
* **Example AI Response:** "That looks like a Socrata API endpoint. To make sure I build exactly what you need, could you please visit the JSON URL and provide me with two things: the dataset's official title and a copy of the first row of data? This will ensure I use the correct columns."

### **Rationale**

Using a live API and verifying the data structure are essential for building applications that are accurate, up-to-date, and reflect real-world data. This guide's purpose is to facilitate the creation of functional, data-driven code.

### **Implementation Checklist**

When generating code, ensure the following criteria are met:

* \[ \] The code makes an HTTP GET request to a Socrata API endpoint (typically ending in .json).  
* \[ \] The data schema (column names) has been confirmed by the user.  
* \[ \] Query parameters, especially SoQL filters ($where, $select, $limit), are used to refine the request.  
* \[ \] The JSON response from the live API is parsed and processed at runtime.  
* \[ \] An App Token is used when available, passed in the X-App-Token header.  
* \[ \] There are no static variables or objects containing pre-fetched Socrata data.
* \[ \] Always use `URLSearchParams` to build query strings. Do not use string concatenation.
* \[ \] Always include `Accept: application/json`.

## **1\. Core Concepts**

### **Finding the Endpoint URL**

The most reliable way to find the endpoint is from the dataset's page on the specific Socrata portal.

1. Navigate to the dataset's page (e.g., on opendata.maryland.gov).  
2. Click the "API" button (it may be under an "Actions" or "..." menu).  
3. The page will display an "API Endpoint". This is your Base URL.

The URL structure is consistent: https://{domain}/resource/{dataset\_identifier}.json

* **Example**: https://data.cdc.gov/resource/cwsq-ngmh.json

### **Authentication (App Tokens)**

While many Socrata datasets are public, using an App Token is highly recommended. It prevents your application from being throttled and identifies your application to the data provider.

* **How to get one**: Register for an account on the specific data portal. You can create and manage App Tokens in your user profile.  
* **How to use it**: Pass the token as an HTTP header.  
  * **Header Key**: X-App-Token  
  * **Header Value**: YOUR\_APP\_TOKEN\_HERE

For private datasets, you will need to use HTTP Basic Authentication with your portal username and password.

### **Socrata Query Language (SoQL)**

Instead of having many different endpoints, Socrata APIs use a single endpoint per dataset and are customized with URL query parameters using SoQL. These parameters all begin with a dollar sign ($).

## **2\. Querying with SoQL Parameters**

All SoQL parameters are added to the endpoint URL as standard query parameters (e.g., ?param1=value\&param2=value).

### **2.1. Filtering Rows ($where)**

This is the most powerful parameter. It allows you to filter the dataset using SQL-like syntax. The value should be URL-encoded.

* **Parameter**: $where  
* **Usage**: Specify conditions to filter rows. String values must be enclosed in single quotes.  
* **Examples**:  
  * Find data for Maryland: $where=stateabbr \= 'MD'  
  * Find data for a specific year and measure: $where=year \= '2022' AND measureid \= 'FOODINSECU'  
  * Complex filtering: $where=year \= '2022' AND measureid IN('FOODINSECU', 'LACKTRPT')

### **2.2. Selecting Columns ($select)**

Limit the response to only the columns you need.

* **Parameter**: $select  
* **Usage**: A comma-separated list of column API names.  
* **Example**: $select=locationname,measure,data\_value

### **2.3. Limiting Results ($limit)**

Control the maximum number of rows returned. The default is typically 1,000.

* **Parameter**: $limit  
* **Usage**: An integer representing the maximum number of rows.  
* **Example**: $limit=50000

### **2.4. Ordering Results ($order)**

Sort the returned data.

* **Parameter**: $order  
* **Usage**: A comma-separated list of columns to sort by. Add ASC (default) or DESC for direction.  
* **Example**: $order=year DESC, locationname ASC

### **2.5. Full-Text Search ($q)**

Perform a simple text search across all columns in the dataset.

* **Parameter**: $q  
* **Usage**: The text string you want to search for.  
* **Example**: $q=Baltimore

## **3\. Implementation Examples**

### **3.1. Python Example (using `requests`)**

This example fetches data from the CDC PLACES dataset, filters for Maryland, and loads it into a Pandas DataFrame.

```python
import requests
import pandas as pd
import os

# 1. Define the endpoint and key variables
base_url = "https://data.cdc.gov/resource/cwsq-ngmh.json"
year = 2022
measures = ['FOODINSECU', 'LACKTRPT']

# 2. Construct the SoQL $where clause securely
# We join the measures with quotes to fit the SQL IN(...) syntax
measures_str = ','.join([f"'{m}'" for m in measures])
soql_where = f"stateabbr = 'MD' AND year = '{year}' AND measureid IN({measures_str})"

# 3. Use a dictionary for params so 'requests' handles URL encoding automatically
# This prevents errors with spaces or special characters in the query
params = {
    "$where": soql_where,
    "$limit": 10000,
    "$select": "locationname, measureid, data_value"
}

# 4. Set Headers
# 'Accept: application/json' is crucial to ensure the server returns JSON
headers = {
    "Accept": "application/json"
}

# Add the App Token only if it exists in the environment
# This allows the code to run (albeit with lower limits) even without a token
app_token = os.getenv("SOCRATA_APP_TOKEN")
if app_token:
    headers["X-App-Token"] = app_token

try:
    # 5. Make the Request
    response = requests.get(base_url, headers=headers, params=params)
    
    # 6. Robust Error Handling
    # If the status code indicates failure (4xx or 5xx), print the status AND the body.
    # The body often contains the specific Socrata error message (e.g., "query.soql.parsingError").
    if not response.ok:
        print(f"Error Status: {response.status_code}")
        try:
            print(f"Error Details: {response.text}") 
        except:
            pass
        response.raise_for_status() # Raise exception to stop execution

    # 7. Parse Data
    data = response.json()
    
    # Load into Pandas for analysis
    df = pd.DataFrame(data)
    print("Successfully fetched data:")
    print(df.head())

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
```

### **3.2. JavaScript Example (using fetch)**

This example uses the browser/Node.js fetch API to get Maryland population data.

```javascript
// 1. Define the endpoint and token
const endpoint = 'https://opendata.maryland.gov/resource/sk8g-4e43.json';
const appToken = ''; // Or process.env.SOCRATA_APP_TOKEN for Node.js

async function getMarylandPopulation() {
    // 2. Use URLSearchParams for safe URL construction
    // This handles encoding of spaces, special characters, and query syntax automatically.
    // Avoid string concatenation (e.g., endpoint + "?$where=" ...) as it is error-prone.
    const url = new URL(endpoint);
    const params = new URLSearchParams();
    params.append('$where', 'year >= 2000');
    params.append('$order', 'year DESC');
    
    // Attach the params to the URL object
    url.search = params.toString();

    console.log(`Fetching data from: ${url.toString()}`);

    // 3. Configure Options & Headers
    // Always specify 'Accept: application/json'
    const options = {
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        }
    };

    // Add authentication header only if we have a token
    if (appToken) {
        options.headers['X-App-Token'] = appToken;
    }

    try {
        const response = await fetch(url.toString(), options);

        // 4. Robust Error Handling
        // Fetch does not throw on 4xx/5xx errors, so we must check response.ok.
        // Crucially, we await response.text() to see the actual error message from Socrata.
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API Error ${response.status}: ${errorText || response.statusText}`);
        }

        // 5. Parse JSON
        const data = await response.json();
        
        // 6. Handle Empty Results
        if (data.length === 0) {
            console.log("No results found.");
            return;
        }

        console.log(`Successfully fetched ${data.length} records.`);
        return data;

    } catch (error) {
        // 7. User-Friendly Error logging
        console.error("Failed to fetch Socrata data:", error);
        // In a real UI, you would display 'error.message' to the user here
    }
}

getMarylandPopulation();
```