package org.example.Processing;

public class EmpaquetadoPedidos extends Tarea {
    private static final int SLEEP_TIME = 20;

    public EmpaquetadoPedidos(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }

    @Override
    public void run() {
        try {
            logTaskExecution("Empaquetado Comenzado");
            Thread.sleep(SLEEP_TIME);
            logTaskExecution("Empaquetado Completado");
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }
}
