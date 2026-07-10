FROM eclipse-temurin:17-jre-jammy

ARG JMETER_VERSION=5.6.3
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && curl -fsSLO "https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz" \
    && curl -fsSLO "https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz.sha512" \
    && sha512sum -c "apache-jmeter-${JMETER_VERSION}.tgz.sha512" \
    && tar -xzf "apache-jmeter-${JMETER_VERSION}.tgz" -C /opt \
    && rm "apache-jmeter-${JMETER_VERSION}.tgz" "apache-jmeter-${JMETER_VERSION}.tgz.sha512" \
    && rm -rf /var/lib/apt/lists/*

ENV JMETER_HOME=/opt/apache-jmeter-${JMETER_VERSION}
ENV PATH=${JMETER_HOME}/bin:${PATH}
WORKDIR /tests
ENTRYPOINT ["jmeter"]
