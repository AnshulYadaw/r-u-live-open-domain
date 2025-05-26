document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const urlInput = document.getElementById('url-input');
    const checkButton = document.getElementById('check-button');
    const statusIndicator = document.getElementById('status-indicator');
    const statusText = document.getElementById('status-text');
    const responseTime = document.getElementById('response-time');
    const historyList = document.getElementById('history-list');
    
    // Load history from local storage
    let checkHistory = JSON.parse(localStorage.getItem('checkHistory')) || [];
    updateHistoryList();
    
    // Event listeners
    checkButton.addEventListener('click', checkStatus);
    urlInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            checkStatus();
        }
    });
    
    // Check status function
    function checkStatus() {
        const url = formatUrl(urlInput.value.trim());
        
        if (!url) {
            showError('Please enter a valid URL');
            return;
        }
        
        // Update UI to indicate checking
        statusIndicator.className = 'status checking';
        statusText.textContent = 'Checking...';
        responseTime.textContent = '';
        
        const startTime = new Date().getTime();
        
        // Since we can't do actual network requests in this example,
        // we'll simulate a check with a timeout and random result
        setTimeout(() => {
            const endTime = new Date().getTime();
            const elapsed = endTime - startTime;
            
            // Simulate random response time between 50ms and 2000ms
            const simulatedTime = Math.floor(Math.random() * 1950) + 50;
            
            // Simulate different statuses
            const random = Math.random();
            let status, statusClass;
            
            if (random > 0.8) {
                status = 'Offline';
                statusClass = 'offline';
            } else if (random > 0.6) {
                status = 'Slow';
                statusClass = 'slow';
            } else {
                status = 'Online';
                statusClass = 'online';
            }
            
            // Update UI with results
            statusIndicator.className = `status ${statusClass}`;
            statusText.textContent = status;
            responseTime.textContent = `${simulatedTime} ms`;
            
            // Add to history
            addToHistory(url, status, simulatedTime);
            
        }, Math.random() * 1500 + 500); // Simulate network delay
    }
    
    // Format URL (make sure it has http:// or https://)
    function formatUrl(url) {
        if (!url) return '';
        
        url = url.toLowerCase();
        
        // Remove trailing slashes
        while (url.endsWith('/')) {
            url = url.slice(0, -1);
        }
        
        // Add https:// if no protocol is specified
        if (!url.startsWith('http://') && !url.startsWith('https://')) {
            url = 'https://' + url;
        }
        
        return url;
    }
    
    // Show error message in status indicator
    function showError(message) {
        statusIndicator.className = 'status offline';
        statusText.textContent = message;
        responseTime.textContent = '';
    }
    
    // Add a check to history
    function addToHistory(url, status, responseTimeMs) {
        // Create new history item
        const historyItem = {
            url,
            status,
            responseTime: responseTimeMs,
            timestamp: new Date().toISOString()
        };
        
        // Add to beginning of array and limit to 10 items
        checkHistory.unshift(historyItem);
        if (checkHistory.length > 10) {
            checkHistory.pop();
        }
        
        // Save to local storage
        localStorage.setItem('checkHistory', JSON.stringify(checkHistory));
        
        // Update the displayed list
        updateHistoryList();
    }
    
    // Update the history list in the UI
    function updateHistoryList() {
        historyList.innerHTML = '';
        
        if (checkHistory.length === 0) {
            historyList.innerHTML = '<li>No recent checks</li>';
            return;
        }
        
        checkHistory.forEach(item => {
            const displayUrl = new URL(item.url).hostname;
            const statusClass = item.status.toLowerCase();
            
            const listItem = document.createElement('li');
            listItem.className = 'history-item';
            listItem.innerHTML = `
                <span class="history-url">${displayUrl}</span>
                <span class="history-status ${statusClass}">${item.status} (${item.responseTime} ms)</span>
            `;
            
            historyList.appendChild(listItem);
        });
    }
});
