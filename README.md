<img width="912" alt="home_website" src="https://github.com/Daha-hussein/Home_pricen-prediction/assets/120591498/f1869fb3-6933-4913-8f3b-e3a34cebf79b">
<h1>Real Estate Home Price Prediction Website</h1>

<p>This data science project series walks through the step-by-step process of building a real estate home price prediction website. We will start by building a model using sklearn and linear regression, using the home prices dataset from Kaggle.com.</p>

<p>The project consists of three main components:</p>

<ol>
  <li><strong>Model Building</strong>: We will cover various data science concepts such as data loading and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tuning, and k-fold cross-validation. We will use Python, along with libraries such as NumPy and Pandas for data cleaning, and Matplotlib for data visualization.</li>
  
  <li><strong>Python Flask Server</strong>: We will write a Python Flask server that utilizes the saved model to serve HTTP requests. The server will be responsible for predicting the price based on user input.</li>
  
  <li><strong>Website</strong>: The website will be built using HTML, CSS, and JavaScript. It will allow users to enter home square footage, number of bedrooms, and other relevant information. The website will then call the Python Flask server to retrieve the predicted price.</li>
</ol>

<h2>Technology and Tools Used</h2>

<ul>
  <li>Python</li>
  <li>NumPy and Pandas for data cleaning</li>
  <li>Matplotlib for data visualization</li>
  <li>Scikit-learn (sklearn) for model building</li>
  <li>Jupyter Notebook, Visual Studio Code, and PyCharm as IDEs</li>
  <li>Python Flask for the HTTP server</li>
  <li>HTML/CSS/JavaScript for the user interface</li>
  <li>AWS EC2 for cloud deployment</li>
</ul>

<h2>Deployment on AWS EC2</h2>

<p>To deploy the application to the cloud, follow these steps:</p>

<ol>
  <li>Create an EC2 instance using the Amazon console. In the security group, add a rule to allow incoming HTTP traffic.</li>
  
  <li>Connect to your instance using SSH. For example:</li>
  
  <pre><code>ssh -i "C:\Users\Viral\.ssh\Banglore.pem" ubuntu@ec2-3-133-88-210.us-east-2.compute.amazonaws.com</code></pre>
  
  <li>Set up Nginx:</li>
  
  <ul>
    <li>Install Nginx on the EC2 instance using the following commands:</li>
    
    <pre><code>sudo apt-get update
sudo apt-get install nginx</code></pre>
    
    <li>Check the status of Nginx using:</li>
    
    <pre><code>sudo service nginx status</code></pre>
    
    <li>Start/stop/restart Nginx using:</li>
    
    <pre><code>sudo service nginx start
sudo service nginx stop
sudo service nginx restart</code></pre>
  </ul>
  
  <li>Copy all your code files to the EC2 instance. You can use WinSCP for this purpose. Download WinSCP from <a href="https://winscp.net/eng/download.php">here</a>.</li>
  
  <li>Once connected to the EC2 instance from WinSCP, copy all the code files into the <code>/home/ubuntu/</code> folder. The full path of your root folder is now: <code>/home/ubuntu/BangloreHomePrices</code>.</li>
  
  <li>Configure Nginx to load the property website by default:</li>
  
  <ul>
    <li>Create the file <code>/etc/nginx/sites-available/bhp.conf</code> with the following content:</li>
    
    <pre><code>server {
    listen 80;
    server_name bhp;
    root /home/ubuntu/BangloreHomePrices/client;
    index app.html;
    location /api/ {
        rewrite ^/api(.*) $1 break;
        proxy_pass http://127.0.0.1:5000;
    }
}</code></pre>
    
    <li>Create a symlink for this file in the <code>/etc/nginx/sites-enabled</code> directory by running the command:</li>
    
    <pre><code>sudo ln -v -s /etc/nginx/sites-available/bhp.conf</code></pre>
    
    <li>Remove the symlink for the default file in the <code>/etc/nginx/sites-enabled</code> directory using:</li>
    
    <pre><code>sudo unlink default</code></pre>
    
    <li>Restart Nginx:</li>
    
    <pre><code>sudo service nginx restart
</code></pre>
  </ul>
  
  <li>Install Python packages and start the Flask server:</li>
  
  <pre><code>sudo apt-get install python3-pip
sudo pip3 install -r C:/Users/HP/Downloads/home_price/server/requirements.txt
python3 C:/Users/HP/Downloads/home_price/client/server.py</code></pre>
  
  <li>Load your cloud URL in a browser, e.g., <a href="http://ec2-3-133-88-210.us-east-2.compute.amazonaws.com/">http://ec2-3-133-88-210.us-east-2.compute.amazonaws.com/</a>. You should now have a fully functional website running in a production cloud environment.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<p>© All rights reserved 2000-2024, WinSCP.net</p>
