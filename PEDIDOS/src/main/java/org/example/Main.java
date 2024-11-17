package org.example;

import org.example.Pedido.Pedido;
import org.example.Processing.ProcesadorPedidos;

public class Main {
    private static final int NUMERO_PEDIDOS = 50;
    private static final int ESPERA_ACTIVACION=5000;
    public static void main(String[] args) throws InterruptedException {
        Thread.sleep(ESPERA_ACTIVACION);
        ProcesadorPedidos procesador = new ProcesadorPedidos();

        for (int i = 1; i <= NUMERO_PEDIDOS; i++) {
            boolean esUrgente = (i % 5 == 0);
            Pedido pedido = new Pedido(i, esUrgente);
            procesador.procesarPedido(pedido);
        }

        procesador.shutdown();
    }
}
