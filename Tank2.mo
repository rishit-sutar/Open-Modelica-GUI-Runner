within NonInteractingTanks;

model Tank2
  parameter Real A = 1;
  Real h;
  Real Q1;

  FlowConnect flowConnect;

equation
  Q1 = flowConnect.F;
  flowConnect.h = h;
  der(h) = Q1 / A;

end Tank2;
