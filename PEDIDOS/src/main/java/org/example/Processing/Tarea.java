package org.example.Processing;
import java.util.logging.Logger;

public abstract class Tarea implements Comparable<Tarea>, Runnable {
    private static final Logger LOGGER = Logger.getLogger(Tarea.class.getName());
    protected int pedido;
    protected int isUrgente;

    public Tarea(int pedido, boolean isUrgente) {
        this.pedido = pedido;
        this.isUrgente = isUrgente ? 0 : 1;
        logTaskCreation(isUrgente);
    }

    private void logTaskCreation(boolean isUrgente) {
        LOGGER.info(() -> String.format("Nuevo Pedido - ID: %d, Prioridad: %s", 
            pedido, isUrgente));
    }

    protected void logTaskExecution(String status) {
        LOGGER.info(() -> String.format("Task %d %s (Priority: %d)", 
            pedido, status, isUrgente));
    }


    @Override
    public int compareTo(Tarea other) {
        return Integer.compare(this.isUrgente, other.isUrgente);
    }
}