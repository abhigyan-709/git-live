# Use a Debian-based OpenJDK image
FROM openjdk:17-jdk-slim

# Jenkins and environment variables
ENV JENKINS_HOME=/var/jenkins_home \
    JENKINS_VERSION=2.452 \
    JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Create Jenkins user
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins

# Install system dependencies and Jenkins
RUN apt-get update && \
    apt-get install -y curl git gnupg2 unzip sudo ca-certificates && \
    install -d -m 0755 -o root -g root /etc/apt/keyrings && \
    curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | gpg --dearmor -o /etc/apt/keyrings/jenkins.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/jenkins.gpg] https://pkg.jenkins.io/debian-stable binary/" \
        > /etc/apt/sources.list.d/jenkins.list && \
    apt-get update && \
    apt-get install -y jenkins && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set permissions
RUN mkdir -p "$JENKINS_HOME" && chown -R jenkins:jenkins "$JENKINS_HOME"

# Switch to Jenkins user
USER jenkins

# Set working directory
WORKDIR $JENKINS_HOME

# Expose ports
EXPOSE 8080 50000

# Run Jenkins
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]




c1 - 

    1. nginx.conf
    2. html.home 

    c1 - stop 

    