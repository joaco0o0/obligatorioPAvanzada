package org.example.Processing;


public class ProcesamientoPago extends Tarea {
    private static final int SLEEP_TIME = 20;
    public ProcesamientoPago(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }



    @Override
    public void run() {
        try {
            logTaskExecution("Pago en ejecucion");
            Thread.sleep(SLEEP_TIME);
            logTaskExecution("Pago completado");
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }

}
