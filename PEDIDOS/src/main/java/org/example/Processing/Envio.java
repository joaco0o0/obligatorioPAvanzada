package org.example.Processing;

public class Envio extends Tarea {
    private static final int SLEEP_TIME = 20;
    public Envio(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }

    @Override
    public void run() {
        try {
            logTaskExecution("Envio en ejecucion");
            Thread.sleep(SLEEP_TIME);
            logTaskExecution("Envio completado");
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }
}
