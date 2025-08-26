package com.yashas.consumer.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class CdcConsumer {
    @KafkaListener(topics = { "cdc.public.customers", "cdc.public.orders", "cdc.public.products" }, groupId = "cdc-consumer-group")
    public void consume(ConsumerRecord<String, String> record){
        System.out.println("Recieved CDC event: "+record.value());
    }
}