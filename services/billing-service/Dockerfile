FROM maven:3.9.9-eclipse-temurin-21 AS build
WORKDIR /build
COPY services/billing-service/pom.xml .
RUN mvn -q -DskipTests dependency:go-offline
COPY services/billing-service/src src
RUN mvn -q -DskipTests package
FROM eclipse-temurin:21-jre
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=build /build/target/billing-service-1.0.0.jar app.jar
EXPOSE 8083
ENTRYPOINT ["java", "-jar", "app.jar"]

