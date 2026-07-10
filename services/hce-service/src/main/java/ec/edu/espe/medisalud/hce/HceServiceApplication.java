package ec.edu.espe.medisalud.hce;

import org.springframework.amqp.core.Queue;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class HceServiceApplication {
    public static void main(String[] args) { SpringApplication.run(HceServiceApplication.class, args); }
    @Bean Queue eventsQueue() { return new Queue("medisalud.events", true); }
}

